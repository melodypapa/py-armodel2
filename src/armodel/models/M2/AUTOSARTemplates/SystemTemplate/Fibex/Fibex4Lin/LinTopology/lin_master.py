"""LinMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config import (
    LinSlaveConfig,
)


@atp_variant()

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
        """Serialize LinMaster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinMaster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize lin_slaves (list from container "LIN-SLAVES")
        if self.lin_slaves:
            container = ET.Element("LIN-SLAVES")
            for item in self.lin_slaves:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("LinSlaveConfig", package_data):
                    # Simple primitive type
                    child = ET.Element("LIN-SLAVE")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("LinSlaveConfig", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize time_base
        if self.time_base is not None:
            serialized = SerializationHelper.serialize_item(self.time_base, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("TIME-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize time_base_jitter
        if self.time_base_jitter is not None:
            serialized = SerializationHelper.serialize_item(self.time_base_jitter, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("TIME-BASE-JITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "LinMaster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinMaster":
        """Deserialize XML element to LinMaster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinMaster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinMaster, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "LinMaster")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse lin_slaves (list from container "LIN-SLAVES")
        obj.lin_slaves = []
        container = SerializationHelper.find_child_element(inner_elem, "LIN-SLAVES")
        if container is not None:
            for child in container:
                if is_ref:
                    child_tag = SerializationHelper.strip_namespace(child.tag)
                    if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                        child_value = ARRef.deserialize(child)
                    else:
                        child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("LinSlaveConfig", package_data):
                    child_value = child.text
                elif is_enum_type("LinSlaveConfig", package_data):
                    child_value = LinSlaveConfig.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_slaves.append(child_value)

        # Parse time_base
        child = SerializationHelper.find_child_element(inner_elem, "TIME-BASE")
        if child is not None:
            time_base_value = child.text
            obj.time_base = time_base_value

        # Parse time_base_jitter
        child = SerializationHelper.find_child_element(inner_elem, "TIME-BASE-JITTER")
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
