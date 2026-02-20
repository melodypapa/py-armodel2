"""PermissibleSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 256)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class PermissibleSignalPath(SignalPathConstraint):
    """AUTOSAR PermissibleSignalPath."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operations: list[Any]
    physical_channel_refs: list[ARRef]
    signals: list[SwcToSwcSignal]
    def __init__(self) -> None:
        """Initialize PermissibleSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.physical_channel_refs: list[ARRef] = []
        self.signals: list[SwcToSwcSignal] = []

    def serialize(self) -> ET.Element:
        """Serialize PermissibleSignalPath to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PermissibleSignalPath, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operations (list to container "OPERATIONS")
        if self.operations:
            wrapper = ET.Element("OPERATIONS")
            for item in self.operations:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_channel_refs (list to container "PHYSICAL-CHANNEL-REFS")
        if self.physical_channel_refs:
            wrapper = ET.Element("PHYSICAL-CHANNEL-REFS")
            for item in self.physical_channel_refs:
                serialized = ARObject._serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    child_elem = ET.Element("PHYSICAL-CHANNEL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize signals (list to container "SIGNALS")
        if self.signals:
            wrapper = ET.Element("SIGNALS")
            for item in self.signals:
                serialized = ARObject._serialize_item(item, "SwcToSwcSignal")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PermissibleSignalPath":
        """Deserialize XML element to PermissibleSignalPath object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PermissibleSignalPath object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PermissibleSignalPath, cls).deserialize(element)

        # Parse operations (list from container "OPERATIONS")
        obj.operations = []
        container = ARObject._find_child_element(element, "OPERATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.operations.append(child_value)

        # Parse physical_channel_refs (list from container "PHYSICAL-CHANNEL-REFS")
        obj.physical_channel_refs = []
        container = ARObject._find_child_element(element, "PHYSICAL-CHANNEL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physical_channel_refs.append(child_value)

        # Parse signals (list from container "SIGNALS")
        obj.signals = []
        container = ARObject._find_child_element(element, "SIGNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signals.append(child_value)

        return obj



class PermissibleSignalPathBuilder:
    """Builder for PermissibleSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PermissibleSignalPath = PermissibleSignalPath()

    def build(self) -> PermissibleSignalPath:
        """Build and return PermissibleSignalPath object.

        Returns:
            PermissibleSignalPath instance
        """
        # TODO: Add validation
        return self._obj
