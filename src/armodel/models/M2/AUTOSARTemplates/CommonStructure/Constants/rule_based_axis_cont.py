"""RuleBasedAxisCont AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AxisIndexType,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class RuleBasedAxisCont(ARObject):
    """AUTOSAR RuleBasedAxisCont."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category", None, False, False, CalprmAxisCategoryEnum),  # category
        ("rule_based", None, False, False, any (RuleBasedValue)),  # ruleBased
        ("sw_arraysize", None, False, False, ValueList),  # swArraysize
        ("sw_axis_index", None, True, False, None),  # swAxisIndex
        ("unit", None, False, False, Unit),  # unit
    ]

    def __init__(self) -> None:
        """Initialize RuleBasedAxisCont."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.rule_based: Optional[Any] = None
        self.sw_arraysize: Optional[ValueList] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.unit: Optional[Unit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RuleBasedAxisCont to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleBasedAxisCont":
        """Create RuleBasedAxisCont from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RuleBasedAxisCont instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RuleBasedAxisCont since parent returns ARObject
        return cast("RuleBasedAxisCont", obj)


class RuleBasedAxisContBuilder:
    """Builder for RuleBasedAxisCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleBasedAxisCont = RuleBasedAxisCont()

    def build(self) -> RuleBasedAxisCont:
        """Build and return RuleBasedAxisCont object.

        Returns:
            RuleBasedAxisCont instance
        """
        # TODO: Add validation
        return self._obj
