"""LinMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config import (
    LinSlaveConfig,
)


class LinMaster(ARObject):
    """AUTOSAR LinMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lin_slaves: list[LinSlaveConfig]
    time_base: Optional[TimeValue]
    time_base_jitter: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize LinMaster."""
        super().__init__()
        self.lin_slaves: list[LinSlaveConfig] = []
        self.time_base: Optional[TimeValue] = None
        self.time_base_jitter: Optional[TimeValue] = None
    def serialize(self) -> ET.Element:
        """Serialize LinMaster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize lin_slaves (list to container "LIN-SLAVES")
        if self.lin_slaves:
            wrapper = ET.Element("LIN-SLAVES")
            for item in self.lin_slaves:
                serialized = ARObject._serialize_item(item, "LinSlaveConfig")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize time_base
        if self.time_base is not None:
            serialized = ARObject._serialize_item(self.time_base, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_base_jitter
        if self.time_base_jitter is not None:
            serialized = ARObject._serialize_item(self.time_base_jitter, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-BASE-JITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinMaster":
        """Deserialize XML element to LinMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinMaster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lin_slaves (list from container "LIN-SLAVES")
        obj.lin_slaves = []
        container = ARObject._find_child_element(element, "LIN-SLAVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_slaves.append(child_value)

        # Parse time_base
        child = ARObject._find_child_element(element, "TIME-BASE")
        if child is not None:
            time_base_value = child.text
            obj.time_base = time_base_value

        # Parse time_base_jitter
        child = ARObject._find_child_element(element, "TIME-BASE-JITTER")
        if child is not None:
            time_base_jitter_value = child.text
            obj.time_base_jitter = time_base_jitter_value

        return obj



class LinMasterBuilder:
    """Builder for LinMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinMaster = LinMaster()

    def build(self) -> LinMaster:
        """Build and return LinMaster object.

        Returns:
            LinMaster instance
        """
        # TODO: Add validation
        return self._obj
