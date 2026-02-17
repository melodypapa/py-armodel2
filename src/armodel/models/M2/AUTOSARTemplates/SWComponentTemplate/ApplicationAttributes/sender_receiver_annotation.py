"""SenderReceiverAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 152)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    DataLimitKindEnum,
    ProcessingKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverAnnotation(GeneralAnnotation):
    """AUTOSAR SenderReceiverAnnotation."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize SenderReceiverAnnotation."""
        super().__init__()
        self.computed: Optional[Boolean] = None
        self.data_element: Optional[VariableDataPrototype] = None
        self.limit_kind: Optional[DataLimitKindEnum] = None
        self.processing_kind_enum: Optional[ProcessingKindEnum] = None


class SenderReceiverAnnotationBuilder:
    """Builder for SenderReceiverAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverAnnotation = SenderReceiverAnnotation()

    def build(self) -> SenderReceiverAnnotation:
        """Build and return SenderReceiverAnnotation object.

        Returns:
            SenderReceiverAnnotation instance
        """
        # TODO: Add validation
        return self._obj
