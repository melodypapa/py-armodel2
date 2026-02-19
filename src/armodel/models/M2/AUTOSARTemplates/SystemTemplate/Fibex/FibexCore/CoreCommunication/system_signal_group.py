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

    system_signals: list[SystemSignal]
    transforming: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize SystemSignalGroup."""
        super().__init__()
        self.system_signals: list[SystemSignal] = []
        self.transforming: Optional[SystemSignal] = None
    def serialize(self) -> ET.Element:
        """Serialize SystemSignalGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SystemSignalGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize system_signals (list to container "SYSTEM-SIGNALS")
        if self.system_signals:
            wrapper = ET.Element("SYSTEM-SIGNALS")
            for item in self.system_signals:
                serialized = ARObject._serialize_item(item, "SystemSignal")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transforming
        if self.transforming is not None:
            serialized = ARObject._serialize_item(self.transforming, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMING")
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

        # Parse system_signals (list from container "SYSTEM-SIGNALS")
        obj.system_signals = []
        container = ARObject._find_child_element(element, "SYSTEM-SIGNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.system_signals.append(child_value)

        # Parse transforming
        child = ARObject._find_child_element(element, "TRANSFORMING")
        if child is not None:
            transforming_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.transforming = transforming_value

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
