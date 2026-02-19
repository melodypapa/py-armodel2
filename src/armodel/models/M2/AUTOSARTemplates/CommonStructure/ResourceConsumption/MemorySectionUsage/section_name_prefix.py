"""SectionNamePrefix AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 147)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 412)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_MemorySectionUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)


class SectionNamePrefix(ImplementationProps):
    """AUTOSAR SectionNamePrefix."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implemented_in_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SectionNamePrefix."""
        super().__init__()
        self.implemented_in_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SectionNamePrefix":
        """Deserialize XML element to SectionNamePrefix object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SectionNamePrefix object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SectionNamePrefix, cls).deserialize(element)

        # Parse implemented_in_ref
        child = ARObject._find_child_element(element, "IMPLEMENTED-IN")
        if child is not None:
            implemented_in_ref_value = ARObject._deserialize_by_tag(child, "DependencyOnArtifact")
            obj.implemented_in_ref = implemented_in_ref_value

        return obj



class SectionNamePrefixBuilder:
    """Builder for SectionNamePrefix."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SectionNamePrefix = SectionNamePrefix()

    def build(self) -> SectionNamePrefix:
        """Build and return SectionNamePrefix object.

        Returns:
            SectionNamePrefix instance
        """
        # TODO: Add validation
        return self._obj
