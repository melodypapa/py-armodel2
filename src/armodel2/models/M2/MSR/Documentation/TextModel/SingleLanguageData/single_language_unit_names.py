"""SingleLanguageUnitNames AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 400)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_SingleLanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextModel.mixed_content_for_unit_names import (
    MixedContentForUnitNames,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SingleLanguageUnitNames(MixedContentForUnitNames):
    """AUTOSAR SingleLanguageUnitNames."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SINGLE-LANGUAGE-UNIT-NAMES"


    def __init__(self) -> None:
        """Initialize SingleLanguageUnitNames."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SingleLanguageUnitNames to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SingleLanguageUnitNames, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "SingleLanguageUnitNames":
        """Deserialize XML element to SingleLanguageUnitNames object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SingleLanguageUnitNames object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SingleLanguageUnitNames, cls).deserialize(element)



class SingleLanguageUnitNamesBuilder(BuilderBase):
    """Builder for SingleLanguageUnitNames with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SingleLanguageUnitNames = SingleLanguageUnitNames()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SingleLanguageUnitNames:
        """Build and return the SingleLanguageUnitNames instance with validation."""
        self._validate_instance()
        return self._obj