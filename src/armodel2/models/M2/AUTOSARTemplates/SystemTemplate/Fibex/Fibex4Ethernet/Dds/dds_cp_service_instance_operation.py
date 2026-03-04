"""DdsCpServiceInstanceOperation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 475)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsCpServiceInstanceOperation(ARObject):
    """AUTOSAR DdsCpServiceInstanceOperation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-CP-SERVICE-INSTANCE-OPERATION"


    dds_operation_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DDS-OPERATION-REF": lambda obj, elem: setattr(obj, "dds_operation_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DdsCpServiceInstanceOperation."""
        super().__init__()
        self.dds_operation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpServiceInstanceOperation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpServiceInstanceOperation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_operation_ref
        if self.dds_operation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_operation_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-OPERATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpServiceInstanceOperation":
        """Deserialize XML element to DdsCpServiceInstanceOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpServiceInstanceOperation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpServiceInstanceOperation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DDS-OPERATION-REF":
                setattr(obj, "dds_operation_ref", ARRef.deserialize(child))

        return obj



class DdsCpServiceInstanceOperationBuilder(BuilderBase):
    """Builder for DdsCpServiceInstanceOperation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpServiceInstanceOperation = DdsCpServiceInstanceOperation()


    def with_dds_operation(self, value: Optional[PduTriggering]) -> "DdsCpServiceInstanceOperationBuilder":
        """Set dds_operation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_operation = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ddsOperation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsCpServiceInstanceOperation:
        """Build and return the DdsCpServiceInstanceOperation instance with validation."""
        self._validate_instance()
        return self._obj