"""ArParameterInImplementationDataInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 324)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class ArParameterInImplementationDataInstanceRef(ARObject):
    """AUTOSAR ArParameterInImplementationDataInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_data_refs: list[Any]
    port_prototype_ref: Optional[ARRef]
    root_parameter_ref: Optional[ARRef]
    target_data_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize ArParameterInImplementationDataInstanceRef."""
        super().__init__()
        self.context_data_refs: list[Any] = []
        self.port_prototype_ref: Optional[ARRef] = None
        self.root_parameter_ref: Optional[ARRef] = None
        self.target_data_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ArParameterInImplementationDataInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize context_data_refs (list to container "CONTEXT-DATA-REFS")
        if self.context_data_refs:
            wrapper = ET.Element("CONTEXT-DATA-REFS")
            for item in self.context_data_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize port_prototype_ref
        if self.port_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.port_prototype_ref, "PortPrototype")
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

        # Serialize root_parameter_ref
        if self.root_parameter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.root_parameter_ref, "ParameterDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-PARAMETER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data_ref
        if self.target_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_data_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArParameterInImplementationDataInstanceRef":
        """Deserialize XML element to ArParameterInImplementationDataInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArParameterInImplementationDataInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_data_refs (list from container "CONTEXT-DATA-REFS")
        obj.context_data_refs = []
        container = SerializationHelper.find_child_element(element, "CONTEXT-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_data_refs.append(child_value)

        # Parse port_prototype_ref
        child = SerializationHelper.find_child_element(element, "PORT-PROTOTYPE-REF")
        if child is not None:
            port_prototype_ref_value = ARRef.deserialize(child)
            obj.port_prototype_ref = port_prototype_ref_value

        # Parse root_parameter_ref
        child = SerializationHelper.find_child_element(element, "ROOT-PARAMETER-REF")
        if child is not None:
            root_parameter_ref_value = ARRef.deserialize(child)
            obj.root_parameter_ref = root_parameter_ref_value

        # Parse target_data_ref
        child = SerializationHelper.find_child_element(element, "TARGET-DATA-REF")
        if child is not None:
            target_data_ref_value = ARRef.deserialize(child)
            obj.target_data_ref = target_data_ref_value

        return obj



class ArParameterInImplementationDataInstanceRefBuilder:
    """Builder for ArParameterInImplementationDataInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArParameterInImplementationDataInstanceRef = ArParameterInImplementationDataInstanceRef()

    def build(self) -> ArParameterInImplementationDataInstanceRef:
        """Build and return ArParameterInImplementationDataInstanceRef object.

        Returns:
            ArParameterInImplementationDataInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
