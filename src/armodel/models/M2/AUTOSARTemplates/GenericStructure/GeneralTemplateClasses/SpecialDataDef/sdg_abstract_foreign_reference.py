"""SdgAbstractForeignReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MetaClassName,
)
from abc import ABC, abstractmethod


class SdgAbstractForeignReference(SdgElementWithGid, ABC):
    """AUTOSAR SdgAbstractForeignReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    dest_meta_class: Optional[MetaClassName]
    def __init__(self) -> None:
        """Initialize SdgAbstractForeignReference."""
        super().__init__()
        self.dest_meta_class: Optional[MetaClassName] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgAbstractForeignReference":
        """Deserialize XML element to SdgAbstractForeignReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgAbstractForeignReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgAbstractForeignReference, cls).deserialize(element)

        # Parse dest_meta_class
        child = ARObject._find_child_element(element, "DEST-META-CLASS")
        if child is not None:
            dest_meta_class_value = child.text
            obj.dest_meta_class = dest_meta_class_value

        return obj



class SdgAbstractForeignReferenceBuilder:
    """Builder for SdgAbstractForeignReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAbstractForeignReference = SdgAbstractForeignReference()

    def build(self) -> SdgAbstractForeignReference:
        """Build and return SdgAbstractForeignReference object.

        Returns:
            SdgAbstractForeignReference instance
        """
        # TODO: Add validation
        return self._obj
