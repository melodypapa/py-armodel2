"""DcmIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import IPduBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    DiagPduType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DcmIPdu(IPdu):
    """AUTOSAR DcmIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DCM-I-PDU"


    diag_pdu_type: Optional[DiagPduType]
    _DESERIALIZE_DISPATCH = {
        "DIAG-PDU-TYPE": lambda obj, elem: setattr(obj, "diag_pdu_type", DiagPduType.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DcmIPdu."""
        super().__init__()
        self.diag_pdu_type: Optional[DiagPduType] = None

    def serialize(self) -> ET.Element:
        """Serialize DcmIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DcmIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diag_pdu_type
        if self.diag_pdu_type is not None:
            serialized = SerializationHelper.serialize_item(self.diag_pdu_type, "DiagPduType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG-PDU-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DcmIPdu":
        """Deserialize XML element to DcmIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DcmIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DcmIPdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIAG-PDU-TYPE":
                setattr(obj, "diag_pdu_type", DiagPduType.deserialize(child))

        return obj



class DcmIPduBuilder(IPduBuilder):
    """Builder for DcmIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DcmIPdu = DcmIPdu()


    def with_diag_pdu_type(self, value: Optional[DiagPduType]) -> "DcmIPduBuilder":
        """Set diag_pdu_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diag_pdu_type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "diagPduType",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DcmIPdu:
        """Build and return the DcmIPdu instance with validation."""
        self._validate_instance()
        return self._obj