#current latest tag is 1.6.1-3.12
FROM mwalbeck/python-poetry

WORKDIR /pypoe

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --no-cache --no-root --without dev

COPY PyPoE PyPoE
COPY export.bash ./

RUN poetry install --no-cache --without dev

RUN mkdir /out /temp
RUN poetry run pypoe_exporter config set out_dir /out 
RUN poetry run pypoe_exporter config set temp_dir /temp
RUN poetry run pypoe_exporter setup perform

ENTRYPOINT [ "poetry", "run" ]
