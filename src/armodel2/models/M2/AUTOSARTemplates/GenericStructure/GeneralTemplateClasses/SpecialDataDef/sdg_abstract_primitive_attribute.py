"""SdgAbstractPrimitiveAttribute AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import SdgElementWithGidBuilder
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SdgAbstractPrimitiveAttribute(SdgElementWithGid, ABC):
    """AUTOSAR SdgAbstractPrimitiveAttribute."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize SdgAbstractPrimitiveAttribute."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SdgAbstractPrimitiveAttribute to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgAbstractPrimitiveAttribute, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "SdgAbstractPrimitiveAttribute":
        """Deserialize XML element to SdgAbstractPrimitiveAttribute object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgAbstractPrimitiveAttribute object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SdgAbstractPrimitiveAttribute, cls).deserialize(element)



class SdgAbstractPrimitiveAttributeBuilder(SdgElementWithGidBuilder):
    """Builder for SdgAbstractPrimitiveAttribute with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SdgAbstractPrimitiveAttribute = SdgAbstractPrimitiveAttribute()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> SdgAbstractPrimitiveAttribute:
        """Build and return the SdgAbstractPrimitiveAttribute instance (abstract)."""
        raise NotImplementedError