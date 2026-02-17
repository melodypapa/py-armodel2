"""Tt AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 318)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class Tt(ARObject):
    """AUTOSAR Tt."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "term": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # term
        "tex_render": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # texRender
        "type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # type
    }

    def __init__(self) -> None:
        """Initialize Tt."""
        super().__init__()
        self.term: String = None
        self.tex_render: Optional[String] = None
        self.type: NameToken = None


class TtBuilder:
    """Builder for Tt."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Tt = Tt()

    def build(self) -> Tt:
        """Build and return Tt object.

        Returns:
            Tt instance
        """
        # TODO: Add validation
        return self._obj
