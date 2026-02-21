"""SystemSignalGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 324)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SystemSignalGroup(ARElement):
    """AUTOSAR SystemSignalGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    system_signal_refs: list[ARRef]
    transforming_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SystemSignalGroup."""
        super().__init__()
        self.system_signal_refs: list[ARRef] = []
        self.transforming_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SystemSignalGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SystemSignalGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize system_signal_refs (list to container "SYSTEM-SIGNAL-REFS")
        if self.system_signal_refs:
            wrapper = ET.Element("SYSTEM-SIGNAL-REFS")
            for item in self.system_signal_refs:
                serialized = SerializationHelper.serialize_item(item, "SystemSignal")
                if serialized is not None:
                    child_elem = ET.Element("SYSTEM-SIGNAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transforming_ref
        if self.transforming_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transforming_ref, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignalGroup":
        """Deserialize XML element to SystemSignalGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SystemSignalGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SystemSignalGroup, cls).deserialize(element)

        # Parse system_signal_refs (list from container "SYSTEM-SIGNAL-REFS")
        obj.system_signal_refs = []
        container = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-REFS")
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
                    obj.system_signal_refs.append(child_value)

        # Parse transforming_ref
        child = SerializationHelper.find_child_element(element, "TRANSFORMING-REF")
        if child is not None:
            transforming_ref_value = ARRef.deserialize(child)
            obj.transforming_ref = transforming_ref_value

        return obj



class SystemSignalGroupBuilder:
    """Builder for SystemSignalGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignalGroup = SystemSignalGroup()

    def build(self) -> SystemSignalGroup:
        """Build and return SystemSignalGroup object.

        Returns:
            SystemSignalGroup instance
        """
        # TODO: Add validation
        return self._obj
