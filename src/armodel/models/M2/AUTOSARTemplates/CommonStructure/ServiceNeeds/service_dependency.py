"""ServiceDependency AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_data_type_assignment import (
    RoleBasedDataTypeAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.symbolic_name_props import (
    SymbolicNameProps,
)


class ServiceDependency(ARObject):
    """AUTOSAR ServiceDependency."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assigned_data", None, False, False, RoleBasedDataTypeAssignment),  # assignedData
        ("diagnostic", None, False, False, ServiceDiagnosticRelevanceEnum),  # diagnostic
        ("symbolic_name_props", None, False, False, SymbolicNameProps),  # symbolicNameProps
    ]

    def __init__(self) -> None:
        """Initialize ServiceDependency."""
        super().__init__()
        self.assigned_data: Optional[RoleBasedDataTypeAssignment] = None
        self.diagnostic: Optional[ServiceDiagnosticRelevanceEnum] = None
        self.symbolic_name_props: Optional[SymbolicNameProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ServiceDependency to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceDependency":
        """Create ServiceDependency from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ServiceDependency instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ServiceDependency since parent returns ARObject
        return cast("ServiceDependency", obj)


class ServiceDependencyBuilder:
    """Builder for ServiceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceDependency = ServiceDependency()

    def build(self) -> ServiceDependency:
        """Build and return ServiceDependency object.

        Returns:
            ServiceDependency instance
        """
        # TODO: Add validation
        return self._obj
