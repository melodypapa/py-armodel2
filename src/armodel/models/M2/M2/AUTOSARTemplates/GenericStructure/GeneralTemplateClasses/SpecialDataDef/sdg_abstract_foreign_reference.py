"""SdgAbstractForeignReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MetaClassName,
)


class SdgAbstractForeignReference(SdgElementWithGid):
    """AUTOSAR SdgAbstractForeignReference."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dest_meta_class": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # destMetaClass
    }

    def __init__(self) -> None:
        """Initialize SdgAbstractForeignReference."""
        super().__init__()
        self.dest_meta_class: Optional[MetaClassName] = None


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
