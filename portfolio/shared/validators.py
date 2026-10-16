from django.core.validators import FileExtensionValidator, URLValidator

validate_image_extension = FileExtensionValidator(
    allowed_extensions=[
        'png',
        'jpg',
        'jpeg',
        'webp',
        'avif',
    ],
)

validate_document_extension = FileExtensionValidator(
    allowed_extensions=['pdf'],
)

validate_vector_extension = FileExtensionValidator(
    allowed_extensions=['svg']
)

validate_url = URLValidator()
