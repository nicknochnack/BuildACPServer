FROM python:3.11-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.8 /uv /uvx /bin/

ENV UV_LINK_MODE=copy
ENV PRODUCTION_MODE=True
ENV UV_CACHE_DIR=/tmp/uvcache

ADD . /app
WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv uv sync

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "server"]