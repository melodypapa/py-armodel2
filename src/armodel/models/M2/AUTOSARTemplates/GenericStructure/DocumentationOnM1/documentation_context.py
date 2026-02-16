"""DocumentationContext AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class DocumentationContext(MultilanguageReferrable):
    """AUTOSAR DocumentationContext."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "feature": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AtpFeature,
        ),  # feature
        "identifiable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Identifiable,
        ),  # identifiable
    }

    def __init__(self) -> None:
        """Initialize DocumentationContext."""
        super().__init__()
        self.feature: Optional[AtpFeature] = None
        self.identifiable: Optional[Identifiable] = None


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
