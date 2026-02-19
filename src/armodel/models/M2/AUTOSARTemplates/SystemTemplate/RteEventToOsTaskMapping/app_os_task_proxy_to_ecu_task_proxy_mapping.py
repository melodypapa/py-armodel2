"""AppOsTaskProxyToEcuTaskProxyMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 209)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
    OsTaskProxy,
)


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """AUTOSAR AppOsTaskProxyToEcuTaskProxyMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    app_task_proxy: Optional[OsTaskProxy]
    ecu_task_proxy: Optional[OsTaskProxy]
    offset: Optional[Integer]
    def __init__(self) -> None:
        """Initialize AppOsTaskProxyToEcuTaskProxyMapping."""
        super().__init__()
        self.app_task_proxy: Optional[OsTaskProxy] = None
        self.ecu_task_proxy: Optional[OsTaskProxy] = None
        self.offset: Optional[Integer] = None
    def serialize(self) -> ET.Element:
        """Serialize AppOsTaskProxyToEcuTaskProxyMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AppOsTaskProxyToEcuTaskProxyMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize app_task_proxy
        if self.app_task_proxy is not None:
            serialized = ARObject._serialize_item(self.app_task_proxy, "OsTaskProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APP-TASK-PROXY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_task_proxy
        if self.ecu_task_proxy is not None:
            serialized = ARObject._serialize_item(self.ecu_task_proxy, "OsTaskProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-TASK-PROXY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset
        if self.offset is not None:
            serialized = ARObject._serialize_item(self.offset, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """Deserialize XML element to AppOsTaskProxyToEcuTaskProxyMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AppOsTaskProxyToEcuTaskProxyMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AppOsTaskProxyToEcuTaskProxyMapping, cls).deserialize(element)

        # Parse app_task_proxy
        child = ARObject._find_child_element(element, "APP-TASK-PROXY")
        if child is not None:
            app_task_proxy_value = ARObject._deserialize_by_tag(child, "OsTaskProxy")
            obj.app_task_proxy = app_task_proxy_value

        # Parse ecu_task_proxy
        child = ARObject._find_child_element(element, "ECU-TASK-PROXY")
        if child is not None:
            ecu_task_proxy_value = ARObject._deserialize_by_tag(child, "OsTaskProxy")
            obj.ecu_task_proxy = ecu_task_proxy_value

        # Parse offset
        child = ARObject._find_child_element(element, "OFFSET")
        if child is not None:
            offset_value = child.text
            obj.offset = offset_value

        return obj



class AppOsTaskProxyToEcuTaskProxyMappingBuilder:
    """Builder for AppOsTaskProxyToEcuTaskProxyMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AppOsTaskProxyToEcuTaskProxyMapping = AppOsTaskProxyToEcuTaskProxyMapping()

    def build(self) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """Build and return AppOsTaskProxyToEcuTaskProxyMapping object.

        Returns:
            AppOsTaskProxyToEcuTaskProxyMapping instance
        """
        # TODO: Add validation
        return self._obj
