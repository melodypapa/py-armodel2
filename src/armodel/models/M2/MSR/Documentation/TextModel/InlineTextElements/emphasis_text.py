"""EmphasisText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 316)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    EEnum,
    EEnumFont,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)


class EmphasisText(ARObject):
    """AUTOSAR EmphasisText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    color: Optional[String]
    font: Optional[EEnumFont]
    sub: Superscript
    sup: Superscript
    tt: Optional[Tt]
    type: Optional[EEnum]
    def __init__(self) -> None:
        """Initialize EmphasisText."""
        super().__init__()
        self.color: Optional[String] = None
        self.font: Optional[EEnumFont] = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.tt: Optional[Tt] = None
        self.type: Optional[EEnum] = None


class EmphasisTextBuilder:
    """Builder for EmphasisText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EmphasisText = EmphasisText()

    def build(self) -> EmphasisText:
        """Build and return EmphasisText object.

        Returns:
            EmphasisText instance
        """
        # TODO: Add validation
        return self._obj
