"""DataPrototypeInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 368)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
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


class DataPrototypeInSystemInstanceRef(ARObject):
    """AUTOSAR DataPrototypeInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_ref: Optional[ARRef]
    context_refs: list[Any]
    context_data_refs: list[Any]
    context_port_ref: Optional[ARRef]
    context_root_ref: Optional[ARRef]
    root_data_prototype_ref: Optional[ARRef]
    target_data_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeInSystemInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_refs: list[Any] = []
        self.context_data_refs: list[Any] = []
        self.context_port_ref: Optional[ARRef] = None
        self.context_root_ref: Optional[ARRef] = None
        self.root_data_prototype_ref: Optional[ARRef] = None
        self.target_data_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeInSystemInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_refs (list to container "CONTEXT-REFS")
        if self.context_refs:
            wrapper = ET.Element("CONTEXT-REFS")
            for item in self.context_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize context_port_ref
        if self.context_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_root_ref
        if self.context_root_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_root_ref, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-ROOT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize root_data_prototype_ref
        if self.root_data_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.root_data_prototype_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-DATA-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data_ref
        if self.target_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_data_ref, "DataPrototype")
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
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInSystemInstanceRef":
        """Deserialize XML element to DataPrototypeInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInSystemInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeInSystemInstanceRef, cls).deserialize(element)

        # Parse base_ref
        child = SerializationHelper.find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse context_refs (list from container "CONTEXT-REFS")
        obj.context_refs = []
        container = SerializationHelper.find_child_element(element, "CONTEXT-REFS")
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
                    obj.context_refs.append(child_value)

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

        # Parse context_port_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-PORT-REF")
        if child is not None:
            context_port_ref_value = ARRef.deserialize(child)
            obj.context_port_ref = context_port_ref_value

        # Parse context_root_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-ROOT-REF")
        if child is not None:
            context_root_ref_value = ARRef.deserialize(child)
            obj.context_root_ref = context_root_ref_value

        # Parse root_data_prototype_ref
        child = SerializationHelper.find_child_element(element, "ROOT-DATA-PROTOTYPE-REF")
        if child is not None:
            root_data_prototype_ref_value = ARRef.deserialize(child)
            obj.root_data_prototype_ref = root_data_prototype_ref_value

        # Parse target_data_ref
        child = SerializationHelper.find_child_element(element, "TARGET-DATA-REF")
        if child is not None:
            target_data_ref_value = ARRef.deserialize(child)
            obj.target_data_ref = target_data_ref_value

        return obj



class DataPrototypeInSystemInstanceRefBuilder:
    """Builder for DataPrototypeInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInSystemInstanceRef = DataPrototypeInSystemInstanceRef()

    def build(self) -> DataPrototypeInSystemInstanceRef:
        """Build and return DataPrototypeInSystemInstanceRef object.

        Returns:
            DataPrototypeInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
