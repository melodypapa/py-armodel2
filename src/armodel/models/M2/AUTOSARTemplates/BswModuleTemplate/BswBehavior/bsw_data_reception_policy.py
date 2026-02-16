"""BswDataReceptionPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BswDataReceptionPolicy(ARObject):
    """AUTOSAR BswDataReceptionPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("received_data", None, False, False, VariableDataPrototype),  # receivedData
    ]

    def __init__(self) -> None:
        """Initialize BswDataReceptionPolicy."""
        super().__init__()
        self.received_data: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswDataReceptionPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswDataReceptionPolicy":
        """Create BswDataReceptionPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswDataReceptionPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswDataReceptionPolicy since parent returns ARObject
        return cast("BswDataReceptionPolicy", obj)


class BswDataReceptionPolicyBuilder:
    """Builder for BswDataReceptionPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswDataReceptionPolicy = BswDataReceptionPolicy()

    def build(self) -> BswDataReceptionPolicy:
        """Build and return BswDataReceptionPolicy object.

        Returns:
            BswDataReceptionPolicy instance
        """
        # TODO: Add validation
        return self._obj
