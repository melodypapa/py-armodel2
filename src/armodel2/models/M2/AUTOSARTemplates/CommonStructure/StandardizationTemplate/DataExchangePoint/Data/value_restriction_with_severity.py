"""ValueRestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import RestrictionWithSeverityBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ValueRestrictionWithSeverity(RestrictionWithSeverity):
    """AUTOSAR ValueRestrictionWithSeverity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VALUE-RESTRICTION-WITH-SEVERITY"


    def __init__(self) -> None:
        """Initialize ValueRestrictionWithSeverity."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize ValueRestrictionWithSeverity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ValueRestrictionWithSeverity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueRestrictionWithSeverity":
        """Deserialize XML element to ValueRestrictionWithSeverity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ValueRestrictionWithSeverity object
        """
        # Delegate to parent class to handle inherited attributes
        return super(ValueRestrictionWithSeverity, cls).deserialize(element)



class ValueRestrictionWithSeverityBuilder(RestrictionWithSeverityBuilder):
    """Builder for ValueRestrictionWithSeverity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ValueRestrictionWithSeverity = ValueRestrictionWithSeverity()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ValueRestrictionWithSeverity:
        """Build and return the ValueRestrictionWithSeverity instance with validation."""
        self._validate_instance()
        return self._obj