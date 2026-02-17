"""TransformationTechnology AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 198)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 764)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    TransformerClassEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.buffer_properties import (
    BufferProperties,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)


class TransformationTechnology(Identifiable):
    """AUTOSAR TransformationTechnology."""

    def __init__(self) -> None:
        """Initialize TransformationTechnology."""
        super().__init__()
        self.buffer_properties: Optional[BufferProperties] = None
        self.has_internal: Optional[Boolean] = None
        self.needs_original: Optional[Boolean] = None
        self.protocol: Optional[String] = None
        self.transformation_description: Optional[TransformationDescription] = None
        self.transformer: Optional[TransformerClassEnum] = None
        self.version: Optional[String] = None


class TransformationTechnologyBuilder:
    """Builder for TransformationTechnology."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationTechnology = TransformationTechnology()

    def build(self) -> TransformationTechnology:
        """Build and return TransformationTechnology object.

        Returns:
            TransformationTechnology instance
        """
        # TODO: Add validation
        return self._obj
