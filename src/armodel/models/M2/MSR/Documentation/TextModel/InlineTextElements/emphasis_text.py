"""EmphasisText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 316)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "color": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # color
        "font": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EEnumFont,
        ),  # font
        "sub": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # sub
        "sup": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # sup
        "tt": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Tt,
        ),  # tt
        "type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EEnum,
        ),  # type
    }

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
