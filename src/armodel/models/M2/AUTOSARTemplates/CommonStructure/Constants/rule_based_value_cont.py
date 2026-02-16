"""RuleBasedValueCont AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class RuleBasedValueCont(ARObject):
    """AUTOSAR RuleBasedValueCont."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rule_based", None, False, False, any (RuleBasedValue)),  # ruleBased
        ("sw_arraysize", None, False, False, ValueList),  # swArraysize
        ("unit", None, False, False, Unit),  # unit
    ]

    def __init__(self) -> None:
        """Initialize RuleBasedValueCont."""
        super().__init__()
        self.rule_based: Optional[Any] = None
        self.sw_arraysize: Optional[ValueList] = None
        self.unit: Optional[Unit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RuleBasedValueCont to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleBasedValueCont":
        """Create RuleBasedValueCont from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RuleBasedValueCont instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RuleBasedValueCont since parent returns ARObject
        return cast("RuleBasedValueCont", obj)


class RuleBasedValueContBuilder:
    """Builder for RuleBasedValueCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleBasedValueCont = RuleBasedValueCont()

    def build(self) -> RuleBasedValueCont:
        """Build and return RuleBasedValueCont object.

        Returns:
            RuleBasedValueCont instance
        """
        # TODO: Add validation
        return self._obj
