"""OperationInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1001)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class OperationInSystemInstanceRef(ARObject):
    """AUTOSAR OperationInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[System]
    context: Optional[RootSwCompositionPrototype]
    context_port_ref: ARRef
    target_operation: Optional[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize OperationInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.context_port_ref: ARRef = None
        self.target_operation: Optional[ClientServerOperation] = None
    def serialize(self) -> ET.Element:
        """Serialize OperationInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize base
        if self.base is not None:
            serialized = ARObject._serialize_item(self.base, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context
        if self.context is not None:
            serialized = ARObject._serialize_item(self.context, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_port_ref
        if self.context_port_ref is not None:
            serialized = ARObject._serialize_item(self.context_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_operation
        if self.target_operation is not None:
            serialized = ARObject._serialize_item(self.target_operation, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-OPERATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OperationInSystemInstanceRef":
        """Deserialize XML element to OperationInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OperationInSystemInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "System")
            obj.base = base_value

        # Parse context
        child = ARObject._find_child_element(element, "CONTEXT")
        if child is not None:
            context_value = ARObject._deserialize_by_tag(child, "RootSwCompositionPrototype")
            obj.context = context_value

        # Parse context_port_ref
        child = ARObject._find_child_element(element, "CONTEXT-PORT")
        if child is not None:
            context_port_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.context_port_ref = context_port_ref_value

        # Parse target_operation
        child = ARObject._find_child_element(element, "TARGET-OPERATION")
        if child is not None:
            target_operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.target_operation = target_operation_value

        return obj



class OperationInSystemInstanceRefBuilder:
    """Builder for OperationInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OperationInSystemInstanceRef = OperationInSystemInstanceRef()

    def build(self) -> OperationInSystemInstanceRef:
        """Build and return OperationInSystemInstanceRef object.

        Returns:
            OperationInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
