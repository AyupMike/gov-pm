"""
Entity to crawl
"""

from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE `entity_to_crawl` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `source_entity` TEXT(255), `name` TEXT(255), `url` TEXT, `reference` TEXT(255), `crawled` INTEGER DEFAULT '0', `timestamp` DATETIME DEFAULT CURRENT_TIMESTAMP)")
]
