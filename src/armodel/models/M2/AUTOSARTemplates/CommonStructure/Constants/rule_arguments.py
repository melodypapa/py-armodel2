"""RuleArguments AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.numerical_or_text import (
    NumericalOrText,
)


class RuleArguments(ARObject):
    """AUTOSAR RuleArguments."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("v", None, True, False, None),  # v
        ("vf", None, True, False, None),  # vf
        ("vt", None, True, False, None),  # vt
        ("vtf", None, False, False, NumericalOrText),  # vtf
    ]

    def __init__(self) -> None:
        """Initialize RuleArguments."""
        super().__init__()
        self.v: Optional[Numerical] = None
        self.vf: Optional[Numerical] = None
        self.vt: Optional[VerbatimString] = None
        self.vtf: Optional[NumericalOrText] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RuleArguments to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleArguments":
        """Create RuleArguments from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RuleArguments instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RuleArguments since parent returns ARObject
        return cast("RuleArguments", obj)


class RuleArgumentsBuilder:
    """Builder for RuleArguments."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleArguments = RuleArguments()

    def build(self) -> RuleArguments:
        """Build and return RuleArguments object.

        Returns:
            RuleArguments instance
        """
        # TODO: Add validation
        return self._obj
