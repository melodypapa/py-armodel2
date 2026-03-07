"""CryptoEllipticCurveProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 564)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CryptoEllipticCurveProps(ARElement):
    """AUTOSAR CryptoEllipticCurveProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CRYPTO-ELLIPTIC-CURVE-PROPS"


    named_curve_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "NAMED-CURVE-ID": lambda obj, elem: setattr(obj, "named_curve_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize CryptoEllipticCurveProps."""
        super().__init__()
        self.named_curve_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoEllipticCurveProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoEllipticCurveProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize named_curve_id
        if self.named_curve_id is not None:
            serialized = SerializationHelper.serialize_item(self.named_curve_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NAMED-CURVE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoEllipticCurveProps":
        """Deserialize XML element to CryptoEllipticCurveProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoEllipticCurveProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoEllipticCurveProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "NAMED-CURVE-ID":
                setattr(obj, "named_curve_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class CryptoEllipticCurvePropsBuilder(ARElementBuilder):
    """Builder for CryptoEllipticCurveProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CryptoEllipticCurveProps = CryptoEllipticCurveProps()


    def with_named_curve_id(self, value: Optional[PositiveInteger]) -> "CryptoEllipticCurvePropsBuilder":
        """Set named_curve_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'named_curve_id' is required and cannot be None")
        self._obj.named_curve_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "namedCurveId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CryptoEllipticCurveProps:
        """Build and return the CryptoEllipticCurveProps instance with validation."""
        self._validate_instance()
        return self._obj