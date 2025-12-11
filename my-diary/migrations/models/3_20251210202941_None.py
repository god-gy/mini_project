from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password_hash" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS "diary" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(100) NOT NULL,
    "content" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "tokenblacklist" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "token" TEXT NOT NULL,
    "expired_at" TIMESTAMPTZ,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "quote" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "content" TEXT NOT NULL,
    "author" VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS "bookmark" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "quote_id" INT NOT NULL REFERENCES "quote" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_bookmark_user_id_46416a" UNIQUE ("user_id", "quote_id")
);
CREATE TABLE IF NOT EXISTS "question" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "question_text" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "userquestion" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "answer_content" TEXT,
    "answered_at" TIMESTAMPTZ,
    "question_id" INT NOT NULL REFERENCES "question" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_userquestio_user_id_e2c439" UNIQUE ("user_id", "question_id")
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztm21v0zoUx79KlVe7EneC3hUmhK7Udd1lF9bBFrgIhCI3cVurid3FDl0F++7YzvPjXd"
    "pmSzS/6+xzEvuXY59/TryfmkMsaNPDE0KWDnCX2uveTw0DB/Ifub5nPQ2sVnGPaGBgakvj"
    "adJqSpkLTMbbZ8CmkDdZkJouWjFEMG/Fnm2LRmJyQ4TncZOH0Y0HDUbmkC2gyzu+fdM8yn"
    "/xzhuPMKh9/85/ImzBW0hFv/hztTRmCNpWavzIEk6y3WCblWw7x+xMGorbTw2T2J6DY+PV"
    "hi0IjqwRZqJ1DjF0AYPi8sz1xHzEcIOph1P0hx6b+ENM+FhwBjybJeZ/TygmwQIoHw2VE5"
    "yLu/zZf3H06uj4r5dHx9xEjiRqeXXnTy+eu+8oCUx07U72AwZ8C4kx5iYxG7XoJV3+n2FI"
    "rApi2BBTjEOpTRhjbCJK61FLeDwlaGLBzpaFoReu9DTAM+JCNMfv4EZyPOcjAtiEBdyCLe"
    "tTcJn28bsLYyBsjbcHF6yjTSwZGnx6fFKQyQmOhtej4elYS0Wevy/uju1jeJ3ucktuRMXg"
    "RPRNgblcA9cyUmEoekifZFoi23yX03eyLQCDuQQgpiEGHaA9RcDdFGVXv6MytVqRyV7zqk"
    "qjzaZRhphdsCpHC+AWs4scMvj4oNu5KHm43xo2xHO24H++eP68gtfn4dXo7fDqgFv9IRcn"
    "D2Q/vCdBV9/vSydVfkcG/fBJY9ThbUkIJly6ArKCmz7+ootBO5Te2ElcBxfDL5Kkswl63l"
    "9O/gnNE3hH7y9PslRdKOZvgAKwp7yHIQeWwE15Zvhageth+KMp2tqbmYdNQbk3IRgeeszE"
    "ZP231swTOL8YX+vDiw+px3A61Meip596BGHrwctMkEcX6f13rr/tiT97Xy8nY0mRUDZ35R"
    "1jO/2ryPEa8Bgx+NwMYCVRhM1hkxKiSog+khB9HD2lkyXEJza/lo0oKxJWGYtKhcWE7TRl"
    "q6RWyxZrpdQSz6+ORogclEIoVgjwdoXcrRRC2nMPCiGIxZbAVmKghatDiYEnLQYk2AIJEA"
    "IvT/zhk1Xpvm3LsSrdi6cmf+folRdXkj77SfqNU0xVVwb3Ka4Mymsrg1xpZQUoXRO+9haA"
    "LuqgzDl2RUSlifYHg3sg5ValTGVfRjc5ANl1YEYOW0F8eG3UEMNc9i3PJDHs8JszzQM/CV"
    "zP3l1BG8hJlubl5Afu9gVtWW5OhZ34RIDgjhyiTxEdhSBf6gyI2e4o8sWDjjLhWzXXqPx1"
    "jI+KijvsCEZIqo/BpTqGpWkFGmEpUaJJbNWK9CZp2dhZmuAe6jhNw2oVYLrmr01bfMnKe3"
    "ZEJDx0tcoHtVW5KuOq6lWPXK8K96W6589SXk+pbqWKfVtAU8W+vR9BiyXLzqfQuigvs/Qy"
    "O1KbyqX+Mb8ClRqd/yuXp9FRQ1UxbdueVqVB1TGqRmSnx7kUJIvyal/s0REl39ARP1Xua1"
    "X5oqp0cb+yRXMlC5Uamk0NkVBhPBXUSRA5R5Um4jSx1QYXFWuF9FaF2iZ2uiF0kbko2ueC"
    "nspdDsQ2ao/r0B73gy+nwpfTcqWWcOnKvvYAn7fF0qgjd33zbgJ82P9n+ff6clL3RcxCJu"
    "v96rX+E2URPzHf6kybTarP0sVmcYGamXb/ieXuNxU/ZzQ="
)
