# Интеграция с основным репозиторием

Ниже пример того, что нужно добавить в основной репозиторий продукта.

## Идея

После merge в `main` продуктовый workflow вычисляет изменённые файлы и вызывает `repository_dispatch` в wiki-репозиторий.

## Пример payload

```json
{
  "event_type": "product-updated",
  "client_payload": {
    "source_repository": "org/product",
    "source_sha": "abcdef123456",
    "changed_files": [
      "src/modules/tasks/service.ts",
      "src/pages/tasks/index.tsx"
    ]
  }
}
```

## Что ещё обычно понадобится

- токен GitHub App или PAT для межрепозиторного вызова
- staging-стенд для автоскриншотов
- тестовый пользователь с устойчивыми правами и данными
