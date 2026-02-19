"""SdgClass AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    MetaClassName,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
    SdgAttribute,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)


class SdgClass(SdgElementWithGid):
    """AUTOSAR SdgClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attributes: list[SdgAttribute]
    caption: Optional[Boolean]
    extends_meta: Optional[MetaClassName]
    sdg_constraints: list[TraceableText]
    def __init__(self) -> None:
        """Initialize SdgClass."""
        super().__init__()
        self.attributes: list[SdgAttribute] = []
        self.caption: Optional[Boolean] = None
        self.extends_meta: Optional[MetaClassName] = None
        self.sdg_constraints: list[TraceableText] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgClass":
        """Deserialize XML element to SdgClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgClass, cls).deserialize(element)

        # Parse attributes (list from container "ATTRIBUTES")
        obj.attributes = []
        container = ARObject._find_child_element(element, "ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.attributes.append(child_value)

        # Parse caption
        child = ARObject._find_child_element(element, "CAPTION")
        if child is not None:
            caption_value = child.text
            obj.caption = caption_value

        # Parse extends_meta
        child = ARObject._find_child_element(element, "EXTENDS-META")
        if child is not None:
            extends_meta_value = child.text
            obj.extends_meta = extends_meta_value

        # Parse sdg_constraints (list from container "SDG-CONSTRAINTS")
        obj.sdg_constraints = []
        container = ARObject._find_child_element(element, "SDG-CONSTRAINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdg_constraints.append(child_value)

        return obj



class SdgClassBuilder:
    """Builder for SdgClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgClass = SdgClass()

    def build(self) -> SdgClass:
        """Build and return SdgClass object.

        Returns:
            SdgClass instance
        """
        # TODO: Add validation
        return self._obj
