"""ArVariableInImplementationDataInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 322)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class ArVariableInImplementationDataInstanceRef(ARObject):
    """AUTOSAR ArVariableInImplementationDataInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_datas: list[Any]
    port_prototype_ref: Optional[ARRef]
    root_variable_ref: Optional[ARRef]
    target_data: Optional[Any]
    def __init__(self) -> None:
        """Initialize ArVariableInImplementationDataInstanceRef."""
        super().__init__()
        self.context_datas: list[Any] = []
        self.port_prototype_ref: Optional[ARRef] = None
        self.root_variable_ref: Optional[ARRef] = None
        self.target_data: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ArVariableInImplementationDataInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize context_datas (list to container "CONTEXT-DATAS")
        if self.context_datas:
            wrapper = ET.Element("CONTEXT-DATAS")
            for item in self.context_datas:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize port_prototype_ref
        if self.port_prototype_ref is not None:
            serialized = ARObject._serialize_item(self.port_prototype_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize root_variable_ref
        if self.root_variable_ref is not None:
            serialized = ARObject._serialize_item(self.root_variable_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data
        if self.target_data is not None:
            serialized = ARObject._serialize_item(self.target_data, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArVariableInImplementationDataInstanceRef":
        """Deserialize XML element to ArVariableInImplementationDataInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArVariableInImplementationDataInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_datas (list from container "CONTEXT-DATAS")
        obj.context_datas = []
        container = ARObject._find_child_element(element, "CONTEXT-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_datas.append(child_value)

        # Parse port_prototype_ref
        child = ARObject._find_child_element(element, "PORT-PROTOTYPE-REF")
        if child is not None:
            port_prototype_ref_value = ARRef.deserialize(child)
            obj.port_prototype_ref = port_prototype_ref_value

        # Parse root_variable_ref
        child = ARObject._find_child_element(element, "ROOT-VARIABLE-REF")
        if child is not None:
            root_variable_ref_value = ARRef.deserialize(child)
            obj.root_variable_ref = root_variable_ref_value

        # Parse target_data
        child = ARObject._find_child_element(element, "TARGET-DATA")
        if child is not None:
            target_data_value = child.text
            obj.target_data = target_data_value

        return obj



class ArVariableInImplementationDataInstanceRefBuilder:
    """Builder for ArVariableInImplementationDataInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArVariableInImplementationDataInstanceRef = ArVariableInImplementationDataInstanceRef()

    def build(self) -> ArVariableInImplementationDataInstanceRef:
        """Build and return ArVariableInImplementationDataInstanceRef object.

        Returns:
            ArVariableInImplementationDataInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
