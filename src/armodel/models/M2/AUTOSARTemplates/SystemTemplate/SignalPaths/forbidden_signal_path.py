"""ForbiddenSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 255)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class ForbiddenSignalPath(SignalPathConstraint):
    """AUTOSAR ForbiddenSignalPath."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operations: list[Any]
    physical_channels: list[PhysicalChannel]
    signals: list[SwcToSwcSignal]
    def __init__(self) -> None:
        """Initialize ForbiddenSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.physical_channels: list[PhysicalChannel] = []
        self.signals: list[SwcToSwcSignal] = []
    def serialize(self) -> ET.Element:
        """Serialize ForbiddenSignalPath to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ForbiddenSignalPath, self).serialize()

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

        # Serialize physical_channels (list to container "PHYSICAL-CHANNELS")
        if self.physical_channels:
            wrapper = ET.Element("PHYSICAL-CHANNELS")
            for item in self.physical_channels:
                serialized = ARObject._serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    wrapper.append(serialized)
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
    def deserialize(cls, element: ET.Element) -> "ForbiddenSignalPath":
        """Deserialize XML element to ForbiddenSignalPath object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ForbiddenSignalPath object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ForbiddenSignalPath, cls).deserialize(element)

        # Parse operations (list from container "OPERATIONS")
        obj.operations = []
        container = ARObject._find_child_element(element, "OPERATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.operations.append(child_value)

        # Parse physical_channels (list from container "PHYSICAL-CHANNELS")
        obj.physical_channels = []
        container = ARObject._find_child_element(element, "PHYSICAL-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physical_channels.append(child_value)

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



class ForbiddenSignalPathBuilder:
    """Builder for ForbiddenSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ForbiddenSignalPath = ForbiddenSignalPath()

    def build(self) -> ForbiddenSignalPath:
        """Build and return ForbiddenSignalPath object.

        Returns:
            ForbiddenSignalPath instance
        """
        # TODO: Add validation
        return self._obj
