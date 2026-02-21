"""MacSecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_local_kay_props import (
    MacSecLocalKayProps,
)


class MacSecProps(ARObject):
    """AUTOSAR MacSecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auto_start: Optional[Boolean]
    mac_sec_kay: Optional[MacSecLocalKayProps]
    on_fail: Optional[TimeValue]
    sak_rekey_time: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize MacSecProps."""
        super().__init__()
        self.auto_start: Optional[Boolean] = None
        self.mac_sec_kay: Optional[MacSecLocalKayProps] = None
        self.on_fail: Optional[TimeValue] = None
        self.sak_rekey_time: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize MacSecProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auto_start
        if self.auto_start is not None:
            serialized = SerializationHelper.serialize_item(self.auto_start, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mac_sec_kay
        if self.mac_sec_kay is not None:
            serialized = SerializationHelper.serialize_item(self.mac_sec_kay, "MacSecLocalKayProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-SEC-KAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize on_fail
        if self.on_fail is not None:
            serialized = SerializationHelper.serialize_item(self.on_fail, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ON-FAIL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sak_rekey_time
        if self.sak_rekey_time is not None:
            serialized = SerializationHelper.serialize_item(self.sak_rekey_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SAK-REKEY-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecProps":
        """Deserialize XML element to MacSecProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecProps, cls).deserialize(element)

        # Parse auto_start
        child = SerializationHelper.find_child_element(element, "AUTO-START")
        if child is not None:
            auto_start_value = child.text
            obj.auto_start = auto_start_value

        # Parse mac_sec_kay
        child = SerializationHelper.find_child_element(element, "MAC-SEC-KAY")
        if child is not None:
            mac_sec_kay_value = SerializationHelper.deserialize_by_tag(child, "MacSecLocalKayProps")
            obj.mac_sec_kay = mac_sec_kay_value

        # Parse on_fail
        child = SerializationHelper.find_child_element(element, "ON-FAIL")
        if child is not None:
            on_fail_value = child.text
            obj.on_fail = on_fail_value

        # Parse sak_rekey_time
        child = SerializationHelper.find_child_element(element, "SAK-REKEY-TIME")
        if child is not None:
            sak_rekey_time_value = child.text
            obj.sak_rekey_time = sak_rekey_time_value

        return obj



class MacSecPropsBuilder:
    """Builder for MacSecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecProps = MacSecProps()

    def build(self) -> MacSecProps:
        """Build and return MacSecProps object.

        Returns:
            MacSecProps instance
        """
        # TODO: Add validation
        return self._obj
