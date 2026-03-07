"""CanGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 864)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_CAN.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import AbstractGlobalTimeDomainPropsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR CanGlobalTimeDomainProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-GLOBAL-TIME-DOMAIN-PROPS"


    fup_data_id_list: PositiveInteger
    ofns_data_id_list: PositiveInteger
    ofs_data_id_list: PositiveInteger
    sync_data_id_list: PositiveInteger
    _DESERIALIZE_DISPATCH = {
        "FUP-DATA-ID-LIST": lambda obj, elem: setattr(obj, "fup_data_id_list", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "OFNS-DATA-ID-LIST": lambda obj, elem: setattr(obj, "ofns_data_id_list", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "OFS-DATA-ID-LIST": lambda obj, elem: setattr(obj, "ofs_data_id_list", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SYNC-DATA-ID-LIST": lambda obj, elem: setattr(obj, "sync_data_id_list", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize CanGlobalTimeDomainProps."""
        super().__init__()
        self.fup_data_id_list: PositiveInteger = None
        self.ofns_data_id_list: PositiveInteger = None
        self.ofs_data_id_list: PositiveInteger = None
        self.sync_data_id_list: PositiveInteger = None

    def serialize(self) -> ET.Element:
        """Serialize CanGlobalTimeDomainProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanGlobalTimeDomainProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize fup_data_id_list
        if self.fup_data_id_list is not None:
            serialized = SerializationHelper.serialize_item(self.fup_data_id_list, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUP-DATA-ID-LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ofns_data_id_list
        if self.ofns_data_id_list is not None:
            serialized = SerializationHelper.serialize_item(self.ofns_data_id_list, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFNS-DATA-ID-LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ofs_data_id_list
        if self.ofs_data_id_list is not None:
            serialized = SerializationHelper.serialize_item(self.ofs_data_id_list, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFS-DATA-ID-LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_data_id_list
        if self.sync_data_id_list is not None:
            serialized = SerializationHelper.serialize_item(self.sync_data_id_list, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-DATA-ID-LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanGlobalTimeDomainProps":
        """Deserialize XML element to CanGlobalTimeDomainProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanGlobalTimeDomainProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanGlobalTimeDomainProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FUP-DATA-ID-LIST":
                setattr(obj, "fup_data_id_list", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "OFNS-DATA-ID-LIST":
                setattr(obj, "ofns_data_id_list", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "OFS-DATA-ID-LIST":
                setattr(obj, "ofs_data_id_list", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SYNC-DATA-ID-LIST":
                setattr(obj, "sync_data_id_list", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class CanGlobalTimeDomainPropsBuilder(AbstractGlobalTimeDomainPropsBuilder):
    """Builder for CanGlobalTimeDomainProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanGlobalTimeDomainProps = CanGlobalTimeDomainProps()


    def with_fup_data_id_list(self, value: PositiveInteger) -> "CanGlobalTimeDomainPropsBuilder":
        """Set fup_data_id_list attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'fup_data_id_list' is required and cannot be None")
        self._obj.fup_data_id_list = value
        return self

    def with_ofns_data_id_list(self, value: PositiveInteger) -> "CanGlobalTimeDomainPropsBuilder":
        """Set ofns_data_id_list attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'ofns_data_id_list' is required and cannot be None")
        self._obj.ofns_data_id_list = value
        return self

    def with_ofs_data_id_list(self, value: PositiveInteger) -> "CanGlobalTimeDomainPropsBuilder":
        """Set ofs_data_id_list attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'ofs_data_id_list' is required and cannot be None")
        self._obj.ofs_data_id_list = value
        return self

    def with_sync_data_id_list(self, value: PositiveInteger) -> "CanGlobalTimeDomainPropsBuilder":
        """Set sync_data_id_list attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'sync_data_id_list' is required and cannot be None")
        self._obj.sync_data_id_list = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "fupDataIDList",
        "ofnsDataIDList",
        "ofsDataIDList",
        "syncDataIDList",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "fupDataIDList", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'fupDataIDList' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'fupDataIDList' is None", UserWarning)
        if getattr(self._obj, "ofnsDataIDList", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'ofnsDataIDList' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'ofnsDataIDList' is None", UserWarning)
        if getattr(self._obj, "ofsDataIDList", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'ofsDataIDList' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'ofsDataIDList' is None", UserWarning)
        if getattr(self._obj, "syncDataIDList", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'syncDataIDList' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'syncDataIDList' is None", UserWarning)


    def build(self) -> CanGlobalTimeDomainProps:
        """Build and return the CanGlobalTimeDomainProps instance with validation."""
        self._validate_instance()
        return self._obj