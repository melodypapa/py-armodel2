"""SenderRecCompositeTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SenderRecCompositeTypeMapping(ARObject, ABC):
    """AUTOSAR SenderRecCompositeTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize SenderRecCompositeTypeMapping."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SenderRecCompositeTypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderRecCompositeTypeMapping, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "SenderRecCompositeTypeMapping":
        """Deserialize XML element to SenderRecCompositeTypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecCompositeTypeMapping object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SenderRecCompositeTypeMapping, cls).deserialize(element)



class SenderRecCompositeTypeMappingBuilder(BuilderBase, ABC):
    """Builder for SenderRecCompositeTypeMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderRecCompositeTypeMapping = SenderRecCompositeTypeMapping()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> SenderRecCompositeTypeMapping:
        """Build and return the SenderRecCompositeTypeMapping instance (abstract)."""
        raise NotImplementedError