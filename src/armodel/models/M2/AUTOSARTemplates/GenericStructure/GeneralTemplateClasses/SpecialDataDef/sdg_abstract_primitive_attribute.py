"""SdgAbstractPrimitiveAttribute AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


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



class SdgAbstractPrimitiveAttributeBuilder:
    """Builder for SdgAbstractPrimitiveAttribute."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAbstractPrimitiveAttribute = SdgAbstractPrimitiveAttribute()

    def build(self) -> SdgAbstractPrimitiveAttribute:
        """Build and return SdgAbstractPrimitiveAttribute object.

        Returns:
            SdgAbstractPrimitiveAttribute instance
        """
        # TODO: Add validation
        return self._obj
