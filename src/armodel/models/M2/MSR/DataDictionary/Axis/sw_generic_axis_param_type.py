"""SwGenericAxisParamType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)


class SwGenericAxisParamType(Identifiable):
    """AUTOSAR SwGenericAxisParamType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_constr", None, False, False, DataConstr),  # dataConstr
    ]

    def __init__(self) -> None:
        """Initialize SwGenericAxisParamType."""
        super().__init__()
        self.data_constr: Optional[DataConstr] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwGenericAxisParamType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwGenericAxisParamType":
        """Create SwGenericAxisParamType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwGenericAxisParamType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwGenericAxisParamType since parent returns ARObject
        return cast("SwGenericAxisParamType", obj)


class SwGenericAxisParamTypeBuilder:
    """Builder for SwGenericAxisParamType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwGenericAxisParamType = SwGenericAxisParamType()

    def build(self) -> SwGenericAxisParamType:
        """Build and return SwGenericAxisParamType object.

        Returns:
            SwGenericAxisParamType instance
        """
        # TODO: Add validation
        return self._obj
