"""LinSlave AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_error_response import (
    LinErrorResponse,
)


class LinSlave(ARObject):
    """AUTOSAR LinSlave."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assign_nad", None, True, False, None),  # assignNad
        ("configured_nad", None, True, False, None),  # configuredNad
        ("function_id", None, True, False, None),  # functionId
        ("initial_nad", None, True, False, None),  # initialNad
        ("lin_error_response", None, False, False, LinErrorResponse),  # linErrorResponse
        ("nas_timeout", None, True, False, None),  # nasTimeout
        ("supplier_id", None, True, False, None),  # supplierId
        ("variant_id", None, True, False, None),  # variantId
    ]

    def __init__(self) -> None:
        """Initialize LinSlave."""
        super().__init__()
        self.assign_nad: Optional[Boolean] = None
        self.configured_nad: Optional[Integer] = None
        self.function_id: Optional[PositiveInteger] = None
        self.initial_nad: Optional[Integer] = None
        self.lin_error_response: Optional[LinErrorResponse] = None
        self.nas_timeout: Optional[TimeValue] = None
        self.supplier_id: Optional[PositiveInteger] = None
        self.variant_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinSlave to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSlave":
        """Create LinSlave from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinSlave instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinSlave since parent returns ARObject
        return cast("LinSlave", obj)


class LinSlaveBuilder:
    """Builder for LinSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSlave = LinSlave()

    def build(self) -> LinSlave:
        """Build and return LinSlave object.

        Returns:
            LinSlave instance
        """
        # TODO: Add validation
        return self._obj
