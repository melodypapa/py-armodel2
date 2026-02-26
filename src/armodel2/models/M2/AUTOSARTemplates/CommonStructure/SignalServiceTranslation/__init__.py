"""SignalServiceTranslation module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.signal_service_translation_props import (
        SignalServiceTranslationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.signal_service_translation_props_set import (
        SignalServiceTranslationPropsSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.signal_service_translation_event_props import (
        SignalServiceTranslationEventProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.signal_service_translation_element_props import (
        SignalServiceTranslationElementProps,
    )

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.signal_service_translation_control_enum import (
    SignalServiceTranslationControlEnum,
)

__all__ = [
    "SignalServiceTranslationControlEnum",
    "SignalServiceTranslationElementProps",
    "SignalServiceTranslationEventProps",
    "SignalServiceTranslationProps",
    "SignalServiceTranslationPropsSet",
]
