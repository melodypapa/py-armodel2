"""DocumentationContext AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 327)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_DocumentationOnM1.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class DocumentationContext(MultilanguageReferrable):
    """AUTOSAR DocumentationContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    feature: Optional[AtpFeature]
    identifiable: Optional[Identifiable]
    def __init__(self) -> None:
        """Initialize DocumentationContext."""
        super().__init__()
        self.feature: Optional[AtpFeature] = None
        self.identifiable: Optional[Identifiable] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentationContext":
        """Deserialize XML element to DocumentationContext object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentationContext object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocumentationContext, cls).deserialize(element)

        # Parse feature
        child = ARObject._find_child_element(element, "FEATURE")
        if child is not None:
            feature_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.feature = feature_value

        # Parse identifiable
        child = ARObject._find_child_element(element, "IDENTIFIABLE")
        if child is not None:
            identifiable_value = ARObject._deserialize_by_tag(child, "Identifiable")
            obj.identifiable = identifiable_value

        return obj



class DocumentationContextBuilder:
    """Builder for DocumentationContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentationContext = DocumentationContext()

    def build(self) -> DocumentationContext:
        """Build and return DocumentationContext object.

        Returns:
            DocumentationContext instance
        """
        # TODO: Add validation
        return self._obj
