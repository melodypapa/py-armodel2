"""AppOsTaskProxyToEcuTaskProxyMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 209)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
    OsTaskProxy,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """AUTOSAR AppOsTaskProxyToEcuTaskProxyMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING"


    app_task_proxy_ref: Optional[ARRef]
    ecu_task_proxy_ref: Optional[ARRef]
    offset: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "APP-TASK-PROXY-REF": lambda obj, elem: setattr(obj, "app_task_proxy_ref", ARRef.deserialize(elem)),
        "ECU-TASK-PROXY-REF": lambda obj, elem: setattr(obj, "ecu_task_proxy_ref", ARRef.deserialize(elem)),
        "OFFSET": lambda obj, elem: setattr(obj, "offset", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize AppOsTaskProxyToEcuTaskProxyMapping."""
        super().__init__()
        self.app_task_proxy_ref: Optional[ARRef] = None
        self.ecu_task_proxy_ref: Optional[ARRef] = None
        self.offset: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize AppOsTaskProxyToEcuTaskProxyMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AppOsTaskProxyToEcuTaskProxyMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize app_task_proxy_ref
        if self.app_task_proxy_ref is not None:
            serialized = SerializationHelper.serialize_item(self.app_task_proxy_ref, "OsTaskProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APP-TASK-PROXY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_task_proxy_ref
        if self.ecu_task_proxy_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_task_proxy_ref, "OsTaskProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-TASK-PROXY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset
        if self.offset is not None:
            serialized = SerializationHelper.serialize_item(self.offset, "Integer")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APP-TASK-PROXY-REF":
                setattr(obj, "app_task_proxy_ref", ARRef.deserialize(child))
            elif tag == "ECU-TASK-PROXY-REF":
                setattr(obj, "ecu_task_proxy_ref", ARRef.deserialize(child))
            elif tag == "OFFSET":
                setattr(obj, "offset", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class AppOsTaskProxyToEcuTaskProxyMappingBuilder(IdentifiableBuilder):
    """Builder for AppOsTaskProxyToEcuTaskProxyMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AppOsTaskProxyToEcuTaskProxyMapping = AppOsTaskProxyToEcuTaskProxyMapping()


    def with_app_task_proxy(self, value: Optional[OsTaskProxy]) -> "AppOsTaskProxyToEcuTaskProxyMappingBuilder":
        """Set app_task_proxy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'app_task_proxy' is required and cannot be None")
        self._obj.app_task_proxy = value
        return self

    def with_ecu_task_proxy(self, value: Optional[OsTaskProxy]) -> "AppOsTaskProxyToEcuTaskProxyMappingBuilder":
        """Set ecu_task_proxy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ecu_task_proxy' is required and cannot be None")
        self._obj.ecu_task_proxy = value
        return self

    def with_offset(self, value: Optional[Integer]) -> "AppOsTaskProxyToEcuTaskProxyMappingBuilder":
        """Set offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'offset' is required and cannot be None")
        self._obj.offset = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "appTaskProxy",
        "ecuTaskProxy",
        "offset",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """Build and return the AppOsTaskProxyToEcuTaskProxyMapping instance with validation."""
        self._validate_instance()
        return self._obj