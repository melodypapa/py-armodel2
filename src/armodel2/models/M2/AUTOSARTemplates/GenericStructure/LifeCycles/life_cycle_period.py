"""LifeCyclePeriod AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    RevisionLabelString,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LifeCyclePeriod(ARObject):
    """AUTOSAR LifeCyclePeriod."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIFE-CYCLE-PERIOD"


    ar_release_version: Optional[RevisionLabelString]
    date: Optional[DateTime]
    product_release: Optional[RevisionLabelString]
    _DESERIALIZE_DISPATCH = {
        "AR-RELEASE-VERSION": lambda obj, elem: setattr(obj, "ar_release_version", SerializationHelper.deserialize_by_tag(elem, "RevisionLabelString")),
        "DATE": lambda obj, elem: setattr(obj, "date", SerializationHelper.deserialize_by_tag(elem, "DateTime")),
        "PRODUCT-RELEASE": lambda obj, elem: setattr(obj, "product_release", SerializationHelper.deserialize_by_tag(elem, "RevisionLabelString")),
    }


    def __init__(self) -> None:
        """Initialize LifeCyclePeriod."""
        super().__init__()
        self.ar_release_version: Optional[RevisionLabelString] = None
        self.date: Optional[DateTime] = None
        self.product_release: Optional[RevisionLabelString] = None

    def serialize(self) -> ET.Element:
        """Serialize LifeCyclePeriod to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LifeCyclePeriod, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ar_release_version
        if self.ar_release_version is not None:
            serialized = SerializationHelper.serialize_item(self.ar_release_version, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AR-RELEASE-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize date
        if self.date is not None:
            serialized = SerializationHelper.serialize_item(self.date, "DateTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize product_release
        if self.product_release is not None:
            serialized = SerializationHelper.serialize_item(self.product_release, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRODUCT-RELEASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCyclePeriod":
        """Deserialize XML element to LifeCyclePeriod object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCyclePeriod object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LifeCyclePeriod, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AR-RELEASE-VERSION":
                setattr(obj, "ar_release_version", SerializationHelper.deserialize_by_tag(child, "RevisionLabelString"))
            elif tag == "DATE":
                setattr(obj, "date", SerializationHelper.deserialize_by_tag(child, "DateTime"))
            elif tag == "PRODUCT-RELEASE":
                setattr(obj, "product_release", SerializationHelper.deserialize_by_tag(child, "RevisionLabelString"))

        return obj



class LifeCyclePeriodBuilder(BuilderBase):
    """Builder for LifeCyclePeriod with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LifeCyclePeriod = LifeCyclePeriod()


    def with_ar_release_version(self, value: Optional[RevisionLabelString]) -> "LifeCyclePeriodBuilder":
        """Set ar_release_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ar_release_version' is required and cannot be None")
        self._obj.ar_release_version = value
        return self

    def with_date(self, value: Optional[DateTime]) -> "LifeCyclePeriodBuilder":
        """Set date attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'date' is required and cannot be None")
        self._obj.date = value
        return self

    def with_product_release(self, value: Optional[RevisionLabelString]) -> "LifeCyclePeriodBuilder":
        """Set product_release attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'product_release' is required and cannot be None")
        self._obj.product_release = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "arReleaseVersion",
        "date",
        "productRelease",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LifeCyclePeriod:
        """Build and return the LifeCyclePeriod instance with validation."""
        self._validate_instance()
        return self._obj