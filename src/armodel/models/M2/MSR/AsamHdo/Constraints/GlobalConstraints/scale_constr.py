"""ScaleConstr AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Limit,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class ScaleConstr(ARObject):
    """AUTOSAR ScaleConstr."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("desc", None, False, False, MultiLanguageOverviewParagraph),  # desc
        ("lower_limit", None, True, False, None),  # lowerLimit
        ("short_label", None, True, False, None),  # shortLabel
        ("upper_limit", None, True, False, None),  # upperLimit
        ("validity", None, False, False, any (ScaleConstrValidity)),  # validity
    ]

    def __init__(self) -> None:
        """Initialize ScaleConstr."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.lower_limit: Optional[Limit] = None
        self.short_label: Optional[Identifier] = None
        self.upper_limit: Optional[Limit] = None
        self.validity: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ScaleConstr to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ScaleConstr":
        """Create ScaleConstr from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ScaleConstr instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ScaleConstr since parent returns ARObject
        return cast("ScaleConstr", obj)


class ScaleConstrBuilder:
    """Builder for ScaleConstr."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ScaleConstr = ScaleConstr()

    def build(self) -> ScaleConstr:
        """Build and return ScaleConstr object.

        Returns:
            ScaleConstr instance
        """
        # TODO: Add validation
        return self._obj
