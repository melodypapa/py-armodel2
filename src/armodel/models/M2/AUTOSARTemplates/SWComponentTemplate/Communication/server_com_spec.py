"""ServerComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ServerComSpec(PPortComSpec):
    """AUTOSAR ServerComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation: Optional[ClientServerOperation]
    queue_length: Optional[PositiveInteger]
    transformation_coms: list[Any]
    def __init__(self) -> None:
        """Initialize ServerComSpec."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.queue_length: Optional[PositiveInteger] = None
        self.transformation_coms: list[Any] = []
    def serialize(self) -> ET.Element:
        """Serialize ServerComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ServerComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operation
        if self.operation is not None:
            serialized = ARObject._serialize_item(self.operation, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize queue_length
        if self.queue_length is not None:
            serialized = ARObject._serialize_item(self.queue_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("QUEUE-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_coms (list to container "TRANSFORMATION-COMS")
        if self.transformation_coms:
            wrapper = ET.Element("TRANSFORMATION-COMS")
            for item in self.transformation_coms:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServerComSpec":
        """Deserialize XML element to ServerComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServerComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ServerComSpec, cls).deserialize(element)

        # Parse operation
        child = ARObject._find_child_element(element, "OPERATION")
        if child is not None:
            operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operation = operation_value

        # Parse queue_length
        child = ARObject._find_child_element(element, "QUEUE-LENGTH")
        if child is not None:
            queue_length_value = child.text
            obj.queue_length = queue_length_value

        # Parse transformation_coms (list from container "TRANSFORMATION-COMS")
        obj.transformation_coms = []
        container = ARObject._find_child_element(element, "TRANSFORMATION-COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformation_coms.append(child_value)

        return obj



class ServerComSpecBuilder:
    """Builder for ServerComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServerComSpec = ServerComSpec()

    def build(self) -> ServerComSpec:
        """Build and return ServerComSpec object.

        Returns:
            ServerComSpec instance
        """
        # TODO: Add validation
        return self._obj
