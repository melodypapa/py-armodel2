"""SwcServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 224)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 608)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_port_assignment import (
    RoleBasedPortAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class SwcServiceDependency(ServiceDependency):
    """AUTOSAR SwcServiceDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_datas: list[Any]
    assigned_ports: list[RoleBasedPortAssignment]
    represented_port_ref: Optional[ARRef]
    service_needs: Optional[ServiceNeeds]
    def __init__(self) -> None:
        """Initialize SwcServiceDependency."""
        super().__init__()
        self.assigned_datas: list[Any] = []
        self.assigned_ports: list[RoleBasedPortAssignment] = []
        self.represented_port_ref: Optional[ARRef] = None
        self.service_needs: Optional[ServiceNeeds] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcServiceDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcServiceDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned_datas (list to container "ASSIGNED-DATAS")
        if self.assigned_datas:
            wrapper = ET.Element("ASSIGNED-DATAS")
            for item in self.assigned_datas:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize assigned_ports (list to container "ASSIGNED-PORTS")
        if self.assigned_ports:
            wrapper = ET.Element("ASSIGNED-PORTS")
            for item in self.assigned_ports:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedPortAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize represented_port_ref
        if self.represented_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.represented_port_ref, "PortGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REPRESENTED-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_needs
        if self.service_needs is not None:
            serialized = SerializationHelper.serialize_item(self.service_needs, "ServiceNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-NEEDS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcServiceDependency":
        """Deserialize XML element to SwcServiceDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcServiceDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcServiceDependency, cls).deserialize(element)

        # Parse assigned_datas (list from container "ASSIGNED-DATAS")
        obj.assigned_datas = []
        container = SerializationHelper.find_child_element(element, "ASSIGNED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_datas.append(child_value)

        # Parse assigned_ports (list from container "ASSIGNED-PORTS")
        obj.assigned_ports = []
        container = SerializationHelper.find_child_element(element, "ASSIGNED-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_ports.append(child_value)

        # Parse represented_port_ref
        child = SerializationHelper.find_child_element(element, "REPRESENTED-PORT-REF")
        if child is not None:
            represented_port_ref_value = ARRef.deserialize(child)
            obj.represented_port_ref = represented_port_ref_value

        # Parse service_needs
        child = SerializationHelper.find_child_element(element, "SERVICE-NEEDS")
        if child is not None:
            service_needs_value = SerializationHelper.deserialize_by_tag(child, "ServiceNeeds")
            obj.service_needs = service_needs_value

        return obj



class SwcServiceDependencyBuilder:
    """Builder for SwcServiceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcServiceDependency = SwcServiceDependency()

    def build(self) -> SwcServiceDependency:
        """Build and return SwcServiceDependency object.

        Returns:
            SwcServiceDependency instance
        """
        # TODO: Add validation
        return self._obj
