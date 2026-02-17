"""WhitespaceControlled AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 292)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class WhitespaceControlled(ARObject):
    """AUTOSAR WhitespaceControlled."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "xml_space": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=any (XmlSpaceEnum),
        ),  # xmlSpace
    }

    def __init__(self) -> None:
        """Initialize WhitespaceControlled."""
        super().__init__()
        self.xml_space: Any = None


class WhitespaceControlledBuilder:
    """Builder for WhitespaceControlled."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WhitespaceControlled = WhitespaceControlled()

    def build(self) -> WhitespaceControlled:
        """Build and return WhitespaceControlled object.

        Returns:
            WhitespaceControlled instance
        """
        # TODO: Add validation
        return self._obj
