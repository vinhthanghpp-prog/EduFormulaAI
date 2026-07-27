"""
BaseRepository
Infrastructure layer for SQLite access.
BUILD-023.5A Release
"""

from __future__ import annotations

import sqlite3
from typing import Any, Iterable

from Database.connection import get_connection


class BaseRepository:
    """Base infrastructure repository.

    This class only provides generic database access helpers.
    Business logic and SQL statements belong in concrete repositories.
    """

    def __init__(self) -> None:
        self.conn: sqlite3.Connection = get_connection()
        self.conn.row_factory = sqlite3.Row

    @property
    def cursor(self) -> sqlite3.Cursor:
        """Return a new cursor."""
        return self.conn.cursor()

    def execute(
        self,
        sql: str,
        params: tuple[Any, ...] = (),
    ) -> sqlite3.Cursor:
        """Execute a single SQL statement and commit."""
        try:
            cur = self.cursor
            cur.execute(sql, params)
            self.commit()
            return cur
        except sqlite3.Error:
            self.rollback()
            raise

    def execute_many(
        self,
        sql: str,
        values: Iterable[tuple[Any, ...]],
    ) -> sqlite3.Cursor:
        """Execute executemany() and commit."""
        try:
            cur = self.cursor
            cur.executemany(sql, values)
            self.commit()
            return cur
        except sqlite3.Error:
            self.rollback()
            raise

    def fetch_one(
        self,
        sql: str,
        params: tuple[Any, ...] = (),
    ) -> sqlite3.Row | None:
        """Return one row or None."""
        cur = self.cursor
        cur.execute(sql, params)
        return cur.fetchone()

    def fetch_all(
        self,
        sql: str,
        params: tuple[Any, ...] = (),
    ) -> list[sqlite3.Row]:
        """Return all matching rows."""
        cur = self.cursor
        cur.execute(sql, params)
        return list(cur.fetchall())

    def commit(self) -> None:
        """Commit current transaction."""
        self.conn.commit()

    def rollback(self) -> None:
        """Rollback current transaction."""
        self.conn.rollback()

    def close(self) -> None:
        """Close database connection."""
        if getattr(self, "conn", None):
            self.conn.close()

    def __enter__(self) -> "BaseRepository":
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
        self.close()
        return False

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass
